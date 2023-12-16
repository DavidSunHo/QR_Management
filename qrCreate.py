from qrcode import make

def qr_create(companyName):
    
    # QRCODE를 생성합니다.
    qrImage = make(f"{companyName}")
    print("QR생성이 완료되었습니다.")
    
    return qrImage


if __name__ == "__main__":
    print("qrCreate.py 모듈 파일이 직접 실행됐습니다.")
    img = qr_create("Can_Pick")
    img.save("./qrUtil/temporary_QR_DB/Can_Pick.png")