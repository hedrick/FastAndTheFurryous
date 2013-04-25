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
	}
	
	// Update is called once per frame
	void Update () {
		
		animation["Run"].speed = 4;
		animation.Play();
		animation.CrossFade("Run");
		
		
		float verticalAxis = Input.GetAxis ("Vertical");		
		if(verticalAxis==0)
		{			
		animation["Run"].speed = 0;
		animation.Play();
		animation.CrossFade("Run");					
		}
		else
			animation["Run"].speed=4;
	}
	void OnControllerColliderHit(ControllerColliderHit hit)
	{
		if(hit.moveDirection.y==0 && !audio.isPlaying)
			audio.Play ();
	}
}
