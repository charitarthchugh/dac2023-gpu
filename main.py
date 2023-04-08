from pathlib import Path

import onnxruntime
import wandb
from fastapi import FastAPI, UploadFile

app = FastAPI()


@app.post("/yolo")
def yolo_fmt(
    model: UploadFile,
    run_name: str,
    img_size: int = 640,
):
    # model_file = Path("model.onnx")
    # model_file.write_bytes(model.file.read())

    session = onnxruntime.InferenceSession(model.file.read())


@app.post("/coco")
def coco_fmt(model: UploadFile, img_size):
    pass


if __name__ == "__main__":
    import uvicorn

    uvicorn.run(app)
