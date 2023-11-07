(function(win,doc){
    'use strict';
    //Confirma o delete apresentando uma opção
    if(doc.querySelector('.btnDel')){
        let btnDel = doc.querySelectorAll('.btnDel');
        for(let i=0; i < btnDel.length; i++){
            btnDel[i].addEventListener('click', function(event){
                if(confirm('Deseja mesmo apagar?')){
                   return true;
                }else{
                    event.preventDefault();
                }
            });
        }
    }
    //Ajax do formulário
    if(doc.querySelector('#form')){
        let form = doc.querySelector('#form');
        function sendForm(event)
        {
          event.preventDefault();
          let data = new FormData(form);
          let ajax = new XMLHttpRequest();
          let token = doc.querySelectorAll('input')[0].value;
          ajax.open('POST', form.action);
          ajax.setRequestHeader('X-CSRF-TOKEN', token);
          ajax.onreadystatechange = function()
          {
              if(ajax.status == 200 && ajax.readyState == 4){
                let result = doc.querySelector('#result');
                result.innerHTML = 'Operação concluída com exito!'
                result.classList.add('alert');
                result.classList.add('alert-success');
              } else if(ajax.status == 500 && ajax.readyState == 4){
                let result = doc.querySelector('#result');
                result.innerHTML = 'Operação não concluída!'
                result.classList.add('alert');
                result.classList.add('alert-danger');
              }
          }
          ajax.send(data);
          form.reset();
        }
        form.addEventListener('submit',sendForm,false);
    }

    if(doc.querySelector('#btn_select')){
        let checkbox = document.querySelectorAll('.check');
        let button = document.querySelector('#btn_select');
        
        button.addEventListener('click', () => {
          for(let current of checkbox){
            current.checked = !current.checked
          }
        })
    
    }
    
})(window,document);