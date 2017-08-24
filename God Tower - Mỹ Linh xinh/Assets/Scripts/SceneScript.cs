using System.Collections;
using System.Collections.Generic;
using UnityEngine;
using UnityEngine.UI;

public class SceneScript : MonoBehaviour {

	public Text levelText;
	public InputField inputField;
	public Button submitButton;
	public Text hintText;

	public string levelContent = "LEVELS";
	public string levelNumber;
	public string levelAnswer;

	string answer;
	// Use this for initialization
	void Start () {
		levelText.text = levelContent;
		StartCoroutine (ChangeLevelTextRoutine());
	}
	public void GetInput()
	{
		answer = inputField.text;
		CheckAnswer ();
	}
	public void CheckAnswer()
	{
		if (answer == levelAnswer)
		{
			hintText.text = "Yayyyyyy";

			//TODO: Change scene
		}
		else 
		{
			hintText.text = "WRONGGGGGGGGGGGGGGGGG!!!!!!!!!!!!";
			hintText.color = Color.red;
			inputField.text = "";
			inputField.ActivateInputField ();
		}
	}

	IEnumerator ChangeLevelTextRoutine()
	{
		while(true)
		{
		levelText.text = levelContent;
		//Wait 2 seconds
		yield return new WaitForSeconds (2f);
		levelText.text = levelNumber;
		yield return new WaitForSeconds (2f);
		}
	}

	var Destination : String;

	function LoadScene () {
		Application.LoadLevel (Destination);
	
	// Update is called once per frame
	void Update () {

	}
}
