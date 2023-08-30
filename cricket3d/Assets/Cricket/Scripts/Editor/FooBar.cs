using System.Collections;
using System.Collections.Generic;
using UnityEditor;
using UnityEngine;
using UnityEngine.AI;

public class FooBar : MonoBehaviour
{
    [MenuItem("Cricket/FooBar/LogMeshBoundsSize")]
    public static void LogMeshBoundsSize()
    {
        var obj = Selection.activeGameObject;
        var mesh = obj.GetComponent<MeshRenderer>();
        if (mesh) Debug.Log(mesh.bounds.size.ToString("F6"));
    }
}
