# 🔗 ระบบ API 2 ตัวด้วย Docker Compose

โปรเจกต์นี้เป็นตัวอย่างการสร้าง API 2 ตัวที่สื่อสารกันผ่าน Docker โดยใช้ภาษา Python (FastAPI) และจัดการการ deploy ด้วย `docker-compose.yml`

## รายละเอียดระบบ

- ผู้ใช้งานส่ง Request ไปที่ API1 (`localhost:8000`)
- API1 จะส่ง request ต่อไปยัง API2 (`api2:8001`)
- API2 ตอบกลับข้อความว่า `Hello from API2!`
- API1 รับข้อความจาก API2 และส่งกลับให้ผู้ใช้
- มีการแสดง log บนทั้ง API1 และ API2

## การติดตั้งและรันระบบด้วย Docker Compose

### 1. Clone โครงการ
```bash
git clone https://github.com/channo39mz/BFC_project1.git
cd BFC_project1
