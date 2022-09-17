
  let time = document.getElementById('time')
  let date = document.getElementById('date')
  let audience_value = document.getElementById('audience').value
  let submit = document.getElementById('submit')
  submit.disabled = true

  function check(time, date){
    axios.get(`/check_free_date/${date}/${time}/${audience_value}`)
        .then(function (response) {
            console.log(response.data["result"]);
            if (response.data["result"]){
                submit.disabled = false
            }else{
                submit.disabled = true
            }
        })
        .catch(function (error) {
            console.log(error);
        })
        .then(function () {
            // always executed
        });
  }

  time.oninput = function() {
    // document.getElementById('result').innerHTML = input.value;
    if (date.value){
        check(time.value, date.value);
    }
  };

  date.oninput = function() {
    // document.getElementById('result').innerHTML = input.value;
    if (time.value){
        check(time.value, date.value);
    }
  };

  audience.oninput = function() {
    audience_value = document.getElementById('audience').value
    if (time.value && date.value){
        check(time.value, date.value, audience_value);
    }
  };