#test onnx file from onnxruntime
import numpy as np
import onnxruntime as ort
import pandas as pd
from sklearn.preprocessing import StandardScaler
from deepmlapp.configurations.conf import LOAN_FILE_PATH


def test_onnx(onnx_path, input_data):
    # Create an ONNX Runtime session
    session = ort.InferenceSession(onnx_path)

    # Get the name of the input and output nodes
    input_name = session.get_inputs()[0].name
    output_name = session.get_outputs()[0].name

    # Run inference
    outputs = session.run([output_name], {input_name: input_data})

    return outputs

if __name__ == "__main__":
    # Example usage
    onnx_path = "loan_approval_model.onnx"  # Path to your ONNX model
    '''
    ApplicantID,Salary,CreditScore,Experience,LoanStatus
    A001,47184,462,23,Rejected
    '''
    #create input array for the above data
    input_data = [[47184, 462, 23]]  # Example input data (Salary, CreditScore, Experience)

    # the model was trained on standard-scaled features, so apply the
    # same scaling (fit on the training data) before running inference
    data = pd.read_csv(LOAN_FILE_PATH)
    x = data.drop(['LoanStatus', 'ApplicantID'], axis=1)
    scaler = StandardScaler().fit(x)
    scaled_input = scaler.transform(input_data).astype(np.float32)

    output = test_onnx(onnx_path, scaled_input)
    score = output[0][0][0]
    status = "Approved" if score >= 0.5 else "Rejected"

    print("ONNX model output:", output)
    print(f"Loan approval status: {status} (score={score:.4f})")
