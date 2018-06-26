using System;
using System.Collections;
using System.Collections.Generic;
using UnityEngine;
using UnityEngine.UI;

public class PopUp : MonoBehaviour
{

    public static GameObject Button;
    public GameObject btn;


    public static void PopUpText(String content)
    {
        
        Button.GetComponentInChildren<Text>().text = content;
        
        Button.SetActive(true);


    }

    public static void PopEnd()
    {
        Button.SetActive(false);
    }

    public void Start()
    {
        Button = btn;

    }
}