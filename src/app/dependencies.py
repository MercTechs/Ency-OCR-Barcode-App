from hatchet_sdk import Context, EmptyModel, Hatchet
from pydantic import BaseModel
 
hatchet = Hatchet(debug=True)
 
class SimpleInput(BaseModel):
    message: str
 
@hatchet.task(name="SimpleTask", input_validator=SimpleInput)
def simple(input: SimpleInput, ctx: Context) -> dict[str, str]:
    return {
      "transformed_message": input.message.lower(),
    }

def main() -> None:
  worker = hatchet.worker("test-worker", workflows=[simple])
  worker.start()
 
if __name__ == "__main__":
    main()