from qiskit_aer import Aer
IBM_cloud_backends = Aer.backends(operational=True, min_num_qubits=5)
for i in IBM_cloud_backends:
    print(i)
