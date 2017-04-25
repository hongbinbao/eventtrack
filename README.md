#### Required Software

  * Python 2.7.x
  * Linux VM (test on ubuntu 14.04 64 bit)

#### Required Tool

    pip:
    wget https://bootstrap.pypa.io/get-pip.py --no-check-certificate
    python get-pip.py
    确认安装成功:
    pip -V

    virtualenv:
    pip install virtualenv
    确认安装成功:
    pip show virtualenv

#### 依赖包安装
    
    pip install -r requirements.txt
    
    (re-generate requirements.txt if update "pip freeze > requirements.txt")

#### 数据库初始化

    python manager.py db upgrade

##### 测试

    python manage.py test
    
##### 命令行调试

    python manage.py shell

#### 数据库迁移
    python manage.py db migrate -m "database change note"
    python manage.py db upgrade
    
#### 服务器启动
    cd eventtrack
    source flask_venv/bin/active
    usage: python manage.py runserver [-?] [-h HOST] [-p PORT] [--threaded]
                           [--processes PROCESSES] [--passthrough-errors] [-d]
                           [-D] [-r] [-R]

    Runs the Flask development server i.e. app.run()

    optional arguments:
      -?, --help            show this help message and exit
      -h HOST, --host HOST
      -p PORT, --port PORT
      --threaded
      --processes PROCESSES
      --passthrough-errors
      -d, --debug           enable the Werkzeug debugger (DO NOT use in production
                        code)
      -D, --no-debug        disable the Werkzeug debugger
      -r, --reload          monitor Python files for changes (not 100{'const':
                            True, 'help': 'monitor Python files for changes (not
                            100% safe for production use)', 'option_strings':
                            ['-r', '--reload'], 'dest': 'use_reloader',
                            'required': False, 'nargs': 0, 'choices': None,
                            'default': None, 'prog': 'manage.py runserver',
                            'container': <argparse._ArgumentGroup object at
                            0x7fd6ee14f790>, 'type': None, 'metavar': None}afe for
                            production use)
      -R, --no-reload       do not monitor Python files for changes

