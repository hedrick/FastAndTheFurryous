using UnityEngine;
using System.Collections;

public class Attic_botLight : MonoBehaviour {
	public float speed = 1;
	public float maxDistance = 2;
	// Use this for initialization
	void Start () {
	
	}
	
	// Update is called once per frame
	void Update () {		
		transform.position = new Vector3( Mathf.PingPong(Time.time*speed, maxDistance), transform.position.y, transform.position.z);
		
	}
}
