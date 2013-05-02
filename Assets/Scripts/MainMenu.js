var isQuit=false;

renderer.material.color=Color.orange;
function OnMouseOver(){
	renderer.material.color=Color.red;
}

function OnMouseEnter(){
	renderer.material.color=Color.blue;
}

function OnMouseExit(){
	renderer.material.color=Color.white;
}

function OnMouseUp(){
	if (isQuit==true){
		Application.Quit();
	}
	else{
		Application.LoadLevel(1);
	}	
}