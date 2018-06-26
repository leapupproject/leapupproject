using System.Collections;
using System.Collections.Generic;
using UnityEditor;
using UnityEngine;
using UnityEngine.SceneManagement;
using UnityEngine.UI;

public class PauseMenu : MonoBehaviour {
    public GameObject Panel;
    public Button Exit;
    public Button Connect;
    public Button Resume;
    public Button Callibrate;

    // Use this for initialization
    void Start () {
        Exit.onClick.AddListener(() =>
        {
            Panel.active = false;
            SceneManager.LoadScene(0);
        });
        Connect.onClick.AddListener(() =>
        {
            Panel.active = false;
            WebSocketClient.ConnectToAnlizer();
        });
        Callibrate.onClick.AddListener(() =>
        {
            Panel.active = false;
            WebSocketClient.CallibrationState = false;
            ColorChanger.State = "NoCalibrate";
            WebSocketClient.RequestForCallibration();
        });
        Resume.onClick.AddListener(() =>
        {
            Panel.active = false;
        });
        
    }

    // Update is called once per frame
    void Update()
    {
        if (Input.GetKeyUp(KeyCode.Escape))
        {
            if (Panel.active == false)
                Panel.active = true;
            else
                Panel.active = false;
        }
        if (Input.GetKeyUp(KeyCode.R))
        {
            Panel.active = false;
            WebSocketClient.CallibrationState = false;
            ColorChanger.State = "NoCalibrate";
            WebSocketClient.RequestForCallibration();
        }
    }

}
