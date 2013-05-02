using UnityEngine;
using System.Collections;

public class catSetup : MonoBehaviour {
	public float moveSpeed;
	public float turnSpeed;
	public AudioClip crashSound;
	
	private Vector3 stairs = new Vector3(0.0f,0.7f,-0.7f);
	private Vector3 floor = new Vector3(0.0f,1.0f,0.0f);
	
	// Use this for initialization
	void Start () {
		audio.clip=crashSound;
		animation["Run"].speed = 4;
		animation["Ready"].speed =1;
	}
	
	// Update is called once per frame
	void Update () {
		
		
		//animation.CrossFade("Run");
		
		
		float verticalAxis = Input.GetAxis ("Vertical");		
		if(verticalAxis==0)
		{
			animation.CrossFade("Ready");
		}
		else
		{
			animation.CrossFade("Run");
		}
	}
	void OnControllerColliderHit(ControllerColliderHit hit)
	{
		if(hit.moveDirection.y==0 && !audio.isPlaying)
			audio.Play ();
	}
}
