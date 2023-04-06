import uvicorn

if __name__ == "__main__":
    uvicorn.run(
        "gpt_examples_generator.app:app", host="localhost", port=4848, reload=True
    )
