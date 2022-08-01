set str=machine-order-service
set matchStr=order
echo %str% | findstr %matchStr% >nul && echo yes || echo no
tzutil /g | findstr "China" >nul && (echo yes) || (echo no)
