# Fast API Libraries
from fastapi import FastAPI, Response, Request
from fastapi.staticfiles import StaticFiles
from fastapi.responses import HTMLResponse, JSONResponse
from fastapi.templating import Jinja2Templates
from fastapi_cache import FastAPICache
from fastapi.middleware.cors import CORSMiddleware
from fastapi_cache.backends.redis import RedisBackend
from fastapi_cache.decorator import cache
from motor.motor_asyncio import AsyncIOMotorClient
from contextlib import asynccontextmanager
# Redis Library
from redis.asyncio import Redis
# Email Libraries
from sendgrid import SendGridAPIClient
from sendgrid.helpers.mail import Mail
# Environment Variables
import os
from dotenv import load_dotenv
# Pydantic Libraries
from pydantic import BaseModel, EmailStr, ValidationError
from typing import Union, List, Dict, Any

load_dotenv()


from_email=os.getenv("EMAIL_FROM")
to_emails=os.getenv("EMAIL_TO")
print(from_email, to_emails)


templates = Jinja2Templates(directory="main/templates/main")
# redis_client = Redis(host="localhost", port=6379, decode_responses=True)
conn = AsyncIOMotorClient(os.getenv("MONGODB_URL"))
db = conn.portfolio

# @asynccontextmanager
# async def lifespan(app: FastAPI):
#     FastAPICache.init(RedisBackend(redis_client), prefix="fastapi-cache")
#     yield
#     await redis_client.close()

# app = FastAPI(lifespan=lifespan)


app = FastAPI()

# app.mount("/static", StaticFiles(directory="static"), name="static")
# Add health check endpoint:
@app.get("/health")
async def health_check():
    return {"status": "healthy", "service": "fastapi"}


app.add_middleware(
    CORSMiddleware,
    allow_origins=[
        "http://localhost:8000", 
        "http://127.0.0.1:8000", 
        "http://localhost:8001", 
        "http://127.0.0.1:8001",
        "https://portfolioprofile-avin.work.gd",
        "https://www.portfolioprofile-avin.work.gd"  # Add your production domain
    ],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


@app.get("/certificates", response_class=JSONResponse)
# @cache(expire=300)
async def get_certificates():
    certificates = await db.certificates.find({}, {"_id": 0}).to_list(length=20)
    print("Certificates:", certificates)
    return certificates

@app.get("/skills", response_class=JSONResponse)
# @cache(expire=300)
async def get_skills():
    skills = await db.skills.find({}, {"_id": 0}).to_list(length=20)

    return skills


@app.get("/projects", response_class=JSONResponse)
# @cache(expire=300)
async def get_projects():
    projects = await db.projects.find({}, {"_id": 0}).to_list(length=20)
    # print("Projects:", projects)
    return projects


# Contact form schema
class ContactForm(BaseModel):
    name: str
    email: EmailStr
    message: str


@app.exception_handler(ValidationError)
async def validation_exception_handler(request: Request, exc: ValidationError):
    return JSONResponse(
        status_code=422,
        content={"detail": "Wrong email address entered."}
    )

@app.post("/contact")
async def contact(form: ContactForm):
    await db["contacts"].insert_one(form.model_dump())
    try:
        message = Mail(
        from_email=os.getenv("EMAIL_FROM"),
        to_emails=os.getenv("EMAIL_TO"),
        subject=f"[Portfolio] - New Message From {form.name}",
        html_content=f"""
            <strong>{form.message}</strong><br>
        """
    )

        try:
            
            sg = SendGridAPIClient(os.getenv("SENDGRID_API_KEY"))
            SENDGRID_API_KEY = os.getenv("SENDGRID_API_KEY")
            response = sg.send(message)
            return {"message": "Thank you! Message sent successfully."}
        except Exception as e:
            print("SendGrid Error:", e)
            return {"message": "Failed to send message."}


    except Exception as e:
        print("Email send failed:", e)
        return {"message": "Saved to DB, but failed to send email."}


