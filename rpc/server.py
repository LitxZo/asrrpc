from concurrent import futures
import os
import time
import grpc
import pb.asr_pb2 as asr_pb2
import pb.asr_pb2_grpc as asr_pb2_grpc
from paddlespeech.cli.asr.infer import ASRExecutor
# 实现 proto 文件中定义的 SearchService
class ASRRpc(asr_pb2_grpc.ASRServicer):

    upload_path = "./upload" 
    # 实现 proto 文件中定义的 rpc 调用
    def ASR(self, request, context):
        fname = request.filename
        filebytes = request.audiobytes
        file_path = os.path.join(self.upload_path, fname)
        with open(file_path, "wb") as fo:
            fo.write(filebytes) 
            print("Received file is saved in ", file_path)
        
        asr = ASRExecutor()
        result = asr(audio_file=file_path, force_yes=True) # 支持16k，其它采样率强制转换
        return asr_pb2.AsrResponse(audiotext=result)

def serve():
    # 启动 rpc 服务，这里可定义最大接收和发送大小(单位M)，默认只有4M
    server = grpc.server(futures.ThreadPoolExecutor(max_workers=10), options=[
        ('grpc.max_send_message_length', 100 * 1024 * 1024),
        ('grpc.max_receive_message_length', 100 * 1024 * 1024)])

    asr_pb2_grpc.add_ASRServicer_to_server(ASRRpc(), server)
    server.add_insecure_port('[::]:8080')
    server.start()
    try:
        while True:
            time.sleep(60*60*24) # one day in seconds
    except KeyboardInterrupt:
        server.stop(0)

if __name__ == '__main__':
    serve()