using UnityEngine;
using System.Collections;

public class tardisLight : MonoBehaviour {
	
	public float maxDistance = 5;
	public float speed = 40;
	// Use this for initialization
	void Start () {
	
	}
	
	// Update is called once per frame
	void Update () {
		light.range=Mathf.PingPong (Time.time*speed,maxDistance);	
	}
}
