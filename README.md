# AmiConvert

AmiConvert は、AmiVoice API での音声認識に適したフォーマット（16kHz, 2ch, PCM WAV）へ変換するツールです。

## 📌 概要
本ツールは、様々なフォーマットの音声ファイルを **AmiVoice API** に最適な形式に変換します。

## 🚀 機能
- 音声ファイルのフォーマット情報表示（コーデック・サンプリングレート・チャンネル数）
- AmiVoice API に適したフォーマットか判定
- 必要に応じて **16kHz / 2ch / PCM WAV** に変換
- 直感的なGUI（PyQt6）
- **FFmpeg を利用した音声変換**

## 🔧 動作環境
- **OS:** Windows / Mac / Linux
- **Python:** 3.8 以上
- **ライブラリ:** PyQt6, pydub, FFmpeg

## 🛠️ セットアップ

### 1️⃣ 仮想環境を作成
```bash
python -m venv venv
source venv/bin/activate  # Windowsなら venv\Scripts\activate
