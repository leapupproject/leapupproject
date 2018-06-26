using System;
using System.Collections;
using System.Collections.Generic;
using System.Net;
using System.Net.Sockets;
using System.Text;
using UnityEngine;
using WebSocketSharp;


public class WebSocketClient : MonoBehaviour {

    Queue<byte[]> m_Messages = new Queue<byte[]>();
    static bool m_IsConnected = false;
    string m_Error = null;
    // Use this for initialization
    public static bool CallibrationState = false;
    public string Ip = "127.0.0.1";
    public string Port = "8000";
    private string Adress = "ws://";
    static WebSocketSharp.WebSocket m_Socket;
    void Start () {
        Adress += Ip +":"+ Port;
        m_Socket = new WebSocketSharp.WebSocket(Adress);
        m_Socket.OnMessage += (sender, e) => m_Messages.Enqueue(e.RawData);
        m_Socket.OnOpen += (sender, e) => m_IsConnected = true;
        m_Socket.OnClose += (sender, e) => m_IsConnected = false;
        m_Socket.OnError += (sender, e) => m_Error = e.Message;
        m_Socket.ConnectAsync();
        Debug.Log("Init WebSocket");
         m_Socket.Connect();
        
    }
    void Update()
    {
        var msg = RecvString();
        if (msg != null)
            CommandHandler(msg);
       


        

        //ws.Connect();
        //var s = ws.RecvString();

    }
    public static void RequestForCallibration()
    {
        m_Socket.Send("Calibrate");
    }
    public static void ConnectToAnlizer()
    {
        m_Socket.Connect();
    }
    public byte[] Recv()
    {
        if (m_Messages.Count == 0)
        {

            return null;

        }
        return m_Messages.Dequeue();
    }
    public string RecvString()
    {
        byte[] retval = Recv();
        if (retval == null)
            return null;
        return Encoding.UTF8.GetString(retval);
    }
    public void Send(string msg)
    {
        m_Socket.Send(Encoding.UTF8.GetBytes(msg));
    }
    public void CommandHandler(string message)
    {
        switch (message)
        {
            case "Calibrate":
                CallibrationState = true;
                m_Socket.Send("exercise");
                ColorChanger.State = message;
                break;
            case "Ready":
                ColorChanger.State = message;
                break;
            case "Done":
                ColorChanger.State = message;
                

                break;
            default:
                Debug.Log("Not Recognize Command:"+message);
                break;
        }
    }
    void OnGUI()
    {

        // PopUp.PopUpText("Connect State:" );
        GUI.Box(new Rect(0, 0, Screen.width, Screen.height), "Connect State:"+m_IsConnected+"       Callibration State:"+ CallibrationState);
    }
}
