"""Serve data from data model layer."""

from fastapi import FastAPI, HTTPException

import models_pika as models


def make_server():
    """Build application and configure routes."""
    app = FastAPI()

    @app.get("/")
    def root():
        return models.all_staff()

    @app.get("/col/{name}")
    def column(name: str):
        try:
            return models.column(name)
        except models.ModelException as exc:
            raise HTTPException(status_code=404, detail=f"Error serving column {name}: {exc}")

    @app.get("/row/{staff_id}")
    def row(staff_id: int):
        try:
            return models.row(staff_id)
        except models.ModelException as exc:
            raise HTTPException(status_code=404, detail=f"Error serving row {staff_id}: {exc}")

    return app


app = make_server()
