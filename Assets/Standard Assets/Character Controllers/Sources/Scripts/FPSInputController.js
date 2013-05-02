private var motor: CharacterMotor;
private var  startTime: float;
private var  lapTime: float;
public var turnSpeed: float;
private var bestTime: float = 100;
public var lapFanfare: AudioClip;
public var bestFormatting: GUIStyle;
public var timeFormatting: GUIStyle;

public var testSize:float=520;

function Awake () {
	motor = GetComponent(CharacterMotor);
}

function OnGUI(){
	var bestBoard = new GUIContent();
	var timeBoard = new GUIContent();
	bestBoard.text = "Best: " + (Mathf.Round(bestTime *100)/100);
	timeBoard.text = "Lap: " + (Mathf.Round(lapTime *100)/100);
	if(bestTime != 100)
		GUI.Box(Rect(Screen.width-470,10,560,0), bestBoard,bestFormatting  );
	GUI.Box(Rect(10,10,0,0), timeBoard,timeFormatting  );
	
}

function Update () {
	
	lapTime = Time.time - startTime;
	
	
	// Get the input vector from kayboard or analog stick
	var directionVector = new Vector3(0, 0, Input.GetAxis("Vertical"));
	var horizontalTurn = Input.GetAxis("Horizontal");
	
	if (directionVector != Vector3.zero) {
		// Get the length of the directon vector and then normalize it
		// Dividing by the length is cheaper than normalizing when we already have the length anyway
		var directionLength = directionVector.magnitude;
		directionVector = directionVector / directionLength;
		
		// Make sure the length is no bigger than 1
		directionLength = Mathf.Min(1, directionLength);
		
		// Make the input vector more sensitive towards the extremes and less sensitive in the middle
		// This makes it easier to control slow speeds when using analog sticks
		directionLength = directionLength * directionLength;
		
		// Multiply the normalized direction vector by the modified length
		directionVector = directionVector * directionLength;
	}
	// Apply the direction to the CharacterMotor
	transform.Rotate(0,horizontalTurn*turnSpeed*Time.deltaTime,0);
	motor.inputMoveDirection = transform.rotation * directionVector;
	
	//motor.inputJump = Input.GetButton("Jump");
	
}
function OnTriggerEnter(hit:Collider){
	if(hit.gameObject.tag == "startLine")
	{
		var finalTime = lapTime;
		if(bestTime>finalTime)
			bestTime = finalTime;
		startTime = Time.time;
		audio.PlayOneShot(lapFanfare);
	}
}
// Require a character controller to be attached to the same game object
@script RequireComponent (CharacterMotor)
@script AddComponentMenu ("Character/FPS Input Controller")
