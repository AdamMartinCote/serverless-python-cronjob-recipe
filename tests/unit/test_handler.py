
from scheduled_function import app


def test_lambda_should_output_text_to_stdout(capsys):
    app.lambda_handler({}, {})
    captured = capsys.readouterr()
    assert captured.out is not None
    assert captured.out != ""
