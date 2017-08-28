using System.Collections;
using System.Collections.Generic;
using UnityEngine;
using UnityEngine.EventSystems;

public class Level5Controller : EventTrigger {

	public override void OnBeginDrag(PointerEventData data){
	
	}
	public override void OnDrag(PointEventData data){
	
		Debug.Log ("Dragging");
		Vector3 screenMousePos = Input.mousePosition;

		Vector3 worldSpaceMousePos = Camera.main.ScreenToWorldPoint (Input.mousePosition);

		Vector3 canvasMousePos = transform.parent.InverseTransformPoint (worldSpaceMousePos);
		transform.localPosition = new Vector3 (canvasMousePos.x,
			canvasMousePos.y,
			transform.localPosition.z
		);
	}

}

