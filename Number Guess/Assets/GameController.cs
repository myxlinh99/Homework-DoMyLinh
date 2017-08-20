using System.Collections;
using System.Collections.Generic;
using UnityEngine;
using UnityEngine.UI;


public class GameController : MonoBehaviour {
	public Text DisplayText;
	public Button YesButton;
	public Button LowerButton;
	public Button HigherButton;
	int min = 0;
	int max = 100;
	int result;

	// Use this for initialization
	void Start () {
		Yes ();
	}
	public void Result ()
	{
		result = (min+ max+ 1)/2;
	}
	public void Yes()
	{
		DisplayText.text = "[NEW GAME] Pick a number between 0 and 100 but don't tell me you Puny Human. Is your number 50?";

	}
	public void Lower()
	{
		Result ();
		max = result;
		print (result);
		int NewResult = (min+max+1)/2;
		DisplayText.text = "Is your number " + NewResult + "?";

	}
	public void Higher()
	{
		Result ();
		min = result;
		print (result);
		int NewResult = (min + max + 1) / 2;
		DisplayText.text = "Is your number " + NewResult + "?";
	}
	// Update is called once per frame
	void Update () {
		
	}
}
