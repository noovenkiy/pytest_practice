import os
import subprocess

from typing import Dict


class Calculator:
    # Класс для управления приложением. Запускает файл webcalculator.exe из текущей директории
    cur_dir = os.path.join(os.path.dirname(__file__), "webcalculator.exe")

    def start(self, host: str = "", port: str = "") -> Dict[str, str]:
        # запустить приложение
        if host and port:
            process = subprocess.Popen(
                [self.cur_dir, "start", host, port],
                stdout=subprocess.PIPE,
                stderr=subprocess.PIPE,
                text=True,
            )

        elif host:
            process = subprocess.Popen(
                [self.cur_dir, "start", host],
                stdout=subprocess.PIPE,
                stderr=subprocess.PIPE,
                text=True,
            )

        else:
            process = subprocess.Popen(
                [self.cur_dir, "start"],
                stdout=subprocess.PIPE,
                stderr=subprocess.PIPE,
                text=True,
            )

        res = {"stdout": process.stdout.read(), "stderr": process.stderr.read()}

        return res

    def restart(self) -> Dict[str, str]:
        # перезапустить приложение
        process = subprocess.Popen(
            [self.cur_dir, "restart"],
            stdout=subprocess.PIPE,
            stderr=subprocess.PIPE,
            text=True,
        )
        res = {"stdout": process.stdout.read(), "stderr": process.stderr.read()}

        return res

    def stop(self) -> Dict[str, str]:
        # остановить приложение
        process = subprocess.Popen(
            [self.cur_dir, "stop"],
            stdout=subprocess.PIPE,
            stderr=subprocess.PIPE,
            text=True,
        )
        res = {"stdout": process.stdout.read(), "stderr": process.stderr.read()}

        return res

    def show_log(self) -> str:
        # показать логи
        process = subprocess.Popen(
            [self.cur_dir, "show_log"],
            stdout=subprocess.PIPE,
            text=True,
        )
        res = process.stdout.read()

        return res

    def help(self) -> str:
        # помощь
        process = subprocess.Popen(
            [self.cur_dir, "--help"],
            stdout=subprocess.PIPE,
            text=True,
        )
        res = process.stdout.read()

        return res
