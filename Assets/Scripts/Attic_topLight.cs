using UnityEngine;
using System.Collections;

public class Attic_topLight : MonoBehaviour {
	public float speed = 1;
	public float maxDistance = 2;
	private Vector3 lightOrigin;
	
	// Use this for initialization
	void Start () {
		lightOrigin = light.transform.position;		
	}
	
	// Update is called once per frame
	void Update () {
		//float transDelta = Mathf.PingPong(Time.time*speed,maxDistance)-maxDistance/2;
		float transDelta = -1*(Mathf.Sin(Time.time*speed)*maxDistance);
		transform.position = new Vector3( lightOrigin.x+transDelta, lightOrigin.y, lightOrigin.z);
		
	}
}
