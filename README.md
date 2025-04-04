## HH Clicker  
Кликер, поднимающий резюме на hh в поиске  
Скрипт использует `selenium` и `python`  

### Запуск:  
1. Создать виртуальное окружение `python3 -m venv auto_click_hh`
2. В `auto_click_hh.env` добавить данные для входа на сайт
3. Переместить `auto_click_hh.env` в `/etc/default/`
4. В `auto_click_hh.service` пропитсать пути к бинарнику venv и запускаемому скрипту
5. Переместить `auto_click_hh.service` и `auto_click_hh.timer` в `/etc/systemd/system/`
6. Выролнить `systemctl enable auto_click_hh.service && systemctl enable auto_click_hh.timer`
7. Выполнить `systemctl start auto_click_hh.service && systemctl start auto_click_hh.timer`