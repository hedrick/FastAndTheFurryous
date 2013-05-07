public var isQuit=false;
public var buttonSound:AudioClip;

function Start(){
	audio.clip = buttonSound;
}

function OnMouseOver(){
	renderer.material.color=Color.red;
}

function OnMouseEnter(){
	audio.Play();
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