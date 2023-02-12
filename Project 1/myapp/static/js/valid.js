
		function checkfname()
		{
			var f=document.form.fname.value;
			var reg=/^[A-Za-z]+$/
			if (f=='')
			{
				//alert("please enter first name");
				document.getElementById("fname").innerHTML="Please Enter First name"
			}
			else if(!reg.test(f))
			{
				document.getElementById("fname").innerHTML="Please Enter only Alphabate"	
			}
			else
			{
				document.getElementById("fname").innerHTML=''
			}
		}
		function checkmobile()
		{
			var f=document.form.mobile.value;
			var reg=/^\d{10}$/;
			if (f=='')
			{
				document.getElementById("mobile").innerHTML="Please Enter mobile number"
			}
			else if(!reg.test(f))
			{
				document.getElementById("mobile").innerHTML="Please Enter only digit"	
			}
			else
			{
				document.getElementById("mobile").innerHTML=''
			}
		}
		function checkemail()
		{
			var f=document.form.email.value;
			var reg=/^[A-Za-z0-9-_.]+@[A-Za-z]+\.[A-Za-z]{2,4}$/;
			if (f=='')
			{
				document.getElementById("email").innerHTML="Please Enter your email"
			}
			else if(!reg.test(f))
			{
				document.getElementById("email").innerHTML="Please Enter valid email"	
			}
			else
			{
				document.getElementById("mobile").innerHTML=''
			}
		}
		function checkpassword()
		{
			var f=document.form.Password.value;
			var reg=/^(?=.*\d)(?=.*[a-z])(?=.*[A-Z])(?=.*[^a-zA-Z0-9])(?!.*\s).{8,15}$/;

			if (f=='')
			{
				document.getElementById("password").innerHTML="Please Enter password";
			}
			else if(!reg.test(f))
			{
				document.getElementById("password").innerHTML="Min 1 upper lower,number & special(8,15)";	
			}
			else
			{
				document.getElementById("password").innerHTML='';
			}
		}
	 	function checkcpassword()
		{
			var f1=document.form.Password.value;
			var f2=document.form.CPassword.value;

			if (f2=='')
			{
				document.getElementById("cpassword").innerHTML="Please Enter  confrim password";
			}
			else if(f1 != f2)
			{
				document.getElementById("cpassword").innerHTML="password & confrim password does not matched";	
			}
			else
			{
				document.getElementById("cpassword").innerHTML='';
			}
		}
		