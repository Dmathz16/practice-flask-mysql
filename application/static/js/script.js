const hamBurger = document.querySelector(".toggle-btn");

hamBurger.addEventListener("click", function () {
  document.querySelector("#sidebar").classList.toggle("expand");
});

var token_key = 'token'
var token = null
var username = ''

function set_token(id)
{

  localStorage.removeItem(token_key);
  localStorage.setItem(token_key, id);

}

function get_name()
{

  $.ajax({
    url         : '/authenticate-token/api/',
    type        : 'get',
    data        : { id: token },
    dataType    : 'JSON',
    beforeSend  : function() { }
  }).done(function(res) {
    username = res.username
    $('#user').text(username+'!')
  }).fail(function(err) {
    console.log(err)
    $('#logout').click()[0]
  });

}

function check_token()
{

  token = localStorage.getItem(token_key);
  $('#alert_token').slideUp()
  if (token) {
    get_name()
    $('#alert_token').slideDown()
  }

}

function logout()
{

  localStorage.removeItem(token_key);

}

check_token()