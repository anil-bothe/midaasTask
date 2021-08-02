from rest_framework.response import Response
from rest_framework.views import APIView
import time
from rest_framework.permissions import IsAuthenticated

from app.models import PrimeNo
from app.serializers.prime_no import GenPrimeNoSerializer, PrimeNoSerializer

from utility.prime_no.fast_prime import prime_generator as getFastPrimeNo
from utility.prime_no.gen_prime import prime_generator as getPrimeNo
from utility.constants import FAST_ALGO, GEN_ALGO

class PrimeNoView(APIView):
    permission_classes = [IsAuthenticated]

    def get(self, request):
        prime_no = PrimeNo.objects.all()
        serializer = PrimeNoSerializer(prime_no, many=True)
        return Response({"prime_no": serializer.data})
    
    def post(self, request):
        data = request.data
        
        prime_no = PrimeNo()
        serializer = GenPrimeNoSerializer(data=data)
        result = []
        msg = ''

        try:
            if serializer.is_valid(raise_exception=True):
                start_no = int(data.get('start_no'))
                end_no = int(data.get('end_no'))
                
                start_time = time.perf_counter()
                # if expected result is optimized 
                if int(data.get('algo_id')) == FAST_ALGO:
                    result = getFastPrimeNo(start_no, end_no)
                elif int(data.get('algo_id')) == GEN_ALGO:
                    result = getPrimeNo(start_no, end_no)
                else:
                    result = []
                total_time = time.perf_counter() - start_time
                msg = 'Excution time is %f' % total_time

                # Save into DATABASE 
                if request.user.is_authenticated:
                    prime_no.user = request.user
                prime_no.input_range = start_no, end_no,
                prime_no.algo_id = data.get('algo_id')
                prime_no.elapsed_time = total_time
                prime_no.result = result
                prime_no.save()

                return Response({"success": True, "msg": msg, "result": result})

            return Response({"success": False, "msg": "validation error!"}) 
        except Exception as e:
            msg = str(e.args[0])
            return Response({"success": False, "msg": msg})
