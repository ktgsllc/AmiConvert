import sys
import os
import subprocess
from PyQt6.QtWidgets import QApplication, QWidget, QVBoxLayout, QPushButton, QLabel, QFileDialog, QTextEdit
from pydub.utils import mediainfo

class AudioConverter(QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        self.setWindowTitle("AmiConvert - 音声フォーマット変換")
        self.setGeometry(100, 100, 600, 350)

        layout = QVBoxLayout()
        self.label = QLabel("ファイルを選択してください")
        layout.addWidget(self.label)

        self.btn_select = QPushButton("ファイルを選択")
        self.btn_select.clicked.connect(self.select_file)
        layout.addWidget(self.btn_select)

        self.text_info = QTextEdit()
        self.text_info.setReadOnly(True)
        layout.addWidget(self.text_info)

        self.btn_convert = QPushButton("AmiVoice用に変換")
        self.btn_convert.clicked.connect(self.convert_audio)
        self.btn_convert.setEnabled(False)
        layout.addWidget(self.btn_convert)

        self.setLayout(layout)

    def select_file(self):
        file_path, _ = QFileDialog.getOpenFileName(self, "ファイルを選択", "", "音声ファイル (*.mp3 *.wav *.m4a *.flac *.aac)")
        if file_path:
            self.file_path = file_path
            self.display_file_info(file_path)

    def display_file_info(self, file_path):
        info = mediainfo(file_path)
        sample_rate = int(info.get("sample_rate", 0))
        channels = int(info.get("channels", 0))
        codec = info.get("codec_name", "不明")

        text = f"ファイル名: {os.path.basename(file_path)}\n"
        text += f"フォーマット: {info.get('format_name', '不明')}\n"
        text += f"コーデック: {codec}\n"
        text += f"サンプリングレート: {sample_rate} Hz\n"
        text += f"チャンネル数: {channels}\n"

        if channels == 2 and sample_rate in [8000, 11025, 16000, 22050, 32000, 44100, 48000] and codec in ["pcm_s16le", "pcm_s16be", "pcm_alaw", "pcm_mulaw"]:
            text += "\n✅ 音声認識に適したフォーマットです"
            self.btn_convert.setEnabled(False)
        else:
            text += "\n⚠️ 変換を推奨（16kHz 2ch WAV に変換可能）"
            self.btn_convert.setEnabled(True)

        self.text_info.setText(text)

    def convert_audio(self):
        output_file = os.path.splitext(self.file_path)[0] + "_converted.wav"
        command = [
            "ffmpeg", "-i", self.file_path,
            "-acodec", "pcm_s16le", "-ar", "16000", "-ac", "2",
            output_file
        ]
        try:
            subprocess.run(command, check=True)
            self.text_info.append(f"\n✅ 変換完了: {output_file}")
        except subprocess.CalledProcessError:
            self.text_info.append("\n❌ 変換に失敗しました")

if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = AudioConverter()
    window.show()
    sys.exit(app.exec())
