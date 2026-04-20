from fastapi import FastAPI, Request
from fastapi.responses import HTMLResponse
from fastapi.templating import Jinja2Templates

from pr_model import solve_pressure
from rk_model import calculate_solubility

app = FastAPI()
templates = Jinja2Templates(directory="templates")

@app.get("/", response_class=HTMLResponse)
def home(request: Request):
    return templates.TemplateResponse("index.html", {"request": request})

@app.get("/pressure")
def pressure(T: float, x: float, y: float):
    P = solve_pressure(T, x, y)
    return {"Pressure (MPa)": P}

@app.get("/solubility")
def solubility(T: float, P: float, m: float):
    x_CO2, y_H2O, molality = calculate_solubility(T, P, m)
    return {
        "x_CO2": x_CO2,
        "y_H2O": y_H2O,
        "molality": molality
    }
