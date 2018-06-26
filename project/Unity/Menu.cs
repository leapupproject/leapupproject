using System.Collections;
using System.Collections.Generic;
using UnityEngine;
using UnityEngine.SceneManagement;
using UnityEngine.UI;

public class Menu : MonoBehaviour {
    

    //Make sure to attach these Buttons in the Inspector
    public Button StartB, StopB;

    void Start()
    {


        //Calls the TaskOnClick method when you click the Button
        StartB.onClick.AddListener(()=> {
            SceneManager.LoadScene(1);


        });
        StopB.onClick.AddListener(() =>
        {

            Application.Quit();


        });
        
    }




}

