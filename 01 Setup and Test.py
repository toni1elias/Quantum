from qiskit_ibm_runtime import QiskitRuntimeService
QiskitRuntimeService.save_account(
token="",
instance="crn:v1:bluemix:public:quantum-computing:us-east:a/ea7adc82e6024e3fab8d609be7a24004:d805ce05-20b8-4f05-9c12-275e85465a47::",
overwrite=True
)
service = QiskitRuntimeService()
print(service.backends())
