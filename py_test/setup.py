import sys 
from cx_Freeze import setup , Executable
import os

# 빌드 옵션
buildOptions = dict(
    packages      = ['selenium'],           # run.y에서 사용한 서드파트 모듈을 기술
    excludes      = [],                     # 필요한 모듈 리스트
    include_files = ['chromedriver.exe']    # 파이썬 파일이 아닌 파일 리스트 (ex. dll,exe ...))
)
# 실행 관련 변수
base = None
base = 'Win32GUI' if sys.platform == 'win32' else None
executables = [
    Executable('run.py',base=base , icon='cd_rom.ico')
]
# setup
setup(  name        = 'Kimmira Babo',
        version     = '1.0',
        description = 'This program has been started in 1993...',
        requires    = [],
        options     = dict(build_exe = buildOptions ),
        executables = executables )