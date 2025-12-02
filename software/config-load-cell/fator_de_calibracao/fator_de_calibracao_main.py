from PySide6.QtWidgets import (QApplication, QMainWindow)
# from fator_de_calibracao_cli import get_calibration_factor, list_ports, Receiver
# from ui_fator_de_calibracao import Ui_MainWindow
import fator_de_calibracao_cli as fact_cli
import ui_fator_de_calibracao as fact_ui
import logging

# import sys

class Calibrator:

    def __init__(self):

        self.app = QApplication()
        self.window = QMainWindow()
        self.ui = fact_ui.Ui_MainWindow()

        self.logger = logging.getLogger('Calibrator')

        self.ui.setupUi(self.window)
        self.extend_ui()

        self.window.show()
        self.app.exec()

    def extend_ui(self):
        self.dummy_elements: bool = False
        ...

    def connect_esp(self):
        
        ...


def extend_ui(ui):

    dummy_elements = False
    global com
    # com = None

    def update_port_list():
        ports = fact_cli.list_ports()
        ui.cbox_seriais.clear()
        ui.cbox_seriais.addItems(['dummy-data-4', 'dummy-data-5', 'dummy-data-6',]) if dummy_elements else None 
        ui.cbox_seriais.addItems(ports)

    def get_samples_with_progress(com: fact_cli.Receiver, n_samples: int = 100):

        print("get_sample_with_progress()") if dummy_elements else None 
        samples = []
        sample_count = 0

        while(com.check_connection() and sample_count < n_samples):

            # ui.display_status.text()
            response = int(com.read_response())
            samples.append(response)
            sample_count+=1
            print(f"Sample {sample_count}: {response}")
            ui.progressBar.value = int(float(sample_count/n_samples)*100)

        return samples

    def connect_esp():

        port = str(ui.cbox_seriais.currentText())
        print(f"{port=}")
        global com
        com = fact_cli.Receiver(port)
        print(f"{com=}")
        com.send_command(b'INIT CONFIG\n')
        ui.display_status.setText('Conectado')

    def send_factor():
        print(f"{com=}")
        fator = ui.line_edit_fator.text().strip()
        fator = fator.replace(',', '.')
        comma = f'SET LOAD FACTOR {fator}\n'
        # print("->",repr(comma.encode('utf-8')))
        print(f"-> {comma.strip()}")
        com.serial.write(comma.encode('utf-8'))    
        # com.serial.flushInput()
        # com.serial.flushOutput()
        response = com.read_response()
        print(response)
        i = 0
        while i < 10:
           print(com.read_response()) 
           i+=1

    def calculate_factor():
        print(f"{com=}")

        if com == None:
            return -1

        samples = get_samples_with_progress(com)
        expected_weight = ui.lineEdit_4.text()

        if expected_weight == '':
            return -1

        calibration_factor = fact_cli.get_calibration_factor(samples, int(expected_weight))

        ui.line_edit_fator.setText(str(calibration_factor))

    ports = fact_cli.list_ports()
    ui.cbox_seriais.addItems(['dummy-data-1', 'dummy-data-2', 'dummy-data-3',]) if dummy_elements else None 
    ui.cbox_seriais.addItems(ports)
    
    ui.btn_atualizar.clicked.connect(update_port_list)
    ui.btn_calcular.clicked.connect(calculate_factor)
    ui.btn_conectar.clicked.connect(connect_esp)
    ui.btn_enviar.clicked.connect(send_factor)


if __name__ == '__main__':

    # app = QApplication(sys.argv)
    # window = QMainWindow()

    # ui = fact_ui.Ui_MainWindow()
    # ui.setupUi(window)
    # extend_ui(ui)

    # window.show()
    # app.exec()

    Calibrator()
