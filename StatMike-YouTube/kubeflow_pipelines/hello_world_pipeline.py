from kfp import dsl
from kfp import compiler

@dsl.component
def say_hello(name: str) -> str:
    hello_text = f'Hello, {name}!'
    print(hello_text)
    return hello_text

@dsl.pipeline
def hello_pipeline() -> str:
    hello_task = say_hello(name='Vivek')
    return hello_task.output


compiler.Compiler().compile(hello_pipeline, 'pipeline.yaml')