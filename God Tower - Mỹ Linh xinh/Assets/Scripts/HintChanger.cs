using System.Collections;
using System.Collections.Generic;
using UnityEngine;
using UnityEngine.UI;

public class HintChanger : MonoBehaviour {


	//public Image hint1;
	//public Image hint2;
	public List<Image> hintsList;
	public Button hintButton;

	int hintCurrentIndex = 0;

		

	//Cach 2
	public void OnHintButtonClick()
	{
		hintCurrentIndex = hintCurrentIndex + 1;
		if (hintCurrentIndex == hintsList.Count) {
			hintButton.transform.localScale = new Vector3 (-1, 1, 1);
			hintCurrentIndex = 0;
		} else {
			hintButton.transform.localScale = new Vector3 (1, 1, 1);
		}

		for (int i = 0; i < hintsList.Count; i++) {
			if (i == hintCurrentIndex) {
				hintsList [i].gameObject.SetActive (true);
			} else {
				hintsList [i].gameObject.SetActive (false);
			}
		}
	}
		//public GameObject hint3;
		

	
	// Update is called once per frame
	/*
	public void OnHintButtonClick(){
		if(hintCurrentIndex == 1){
			hint1.gameObject.SetActive (false);
			hint2.gameObject.SetActive (true);
			hintCurrentIndex = 2;
		} else if (hintCurrentIndex==2){
			hint1.gameObject.SetActive (true);
			hint2.gameObject.SetActive (false);
			hintCurrentIndex = 1;

		}

	}

*/


}
