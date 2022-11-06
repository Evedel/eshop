SYNCHRONISATION = [
    {
        "binding": "kubernetes",
        "objects": [
            {
                "filterResult": None,
                "object": {
                    "apiVersion": "v1",
                    "data": {"test": "true"},
                    "kind": "Secret",
                    "metadata": {
                        "annotations": {
                            "kubectl.kubernetes.io/last-applied-configuration": '{"apiVersion":"v1","data":{"test":"true"},"kind":"Secret","metadata":{"annotations":{},"name":"test-secret-1","namespace":"workspace-1"},"type":"Opaque"}\\n'
                        },
                        "creationTimestamp": "2022-11-06T03:28:27Z",
                        "managedFields": [
                            {
                                "apiVersion": "v1",
                                "fieldsType": "FieldsV1",
                                "fieldsV1": {
                                    "f:data": {".": {}, "f:test": {}},
                                    "f:metadata": {
                                        "f:annotations": {
                                            ".": {},
                                            "f:kubectl.kubernetes.io/last-applied-configuration": {},
                                        }
                                    },
                                    "f:type": {},
                                },
                                "manager": "kubectl-client-side-apply",
                                "operation": "Update",
                                "time": "2022-11-06T03:28:27Z",
                            }
                        ],
                        "name": "test-secret-1",
                        "namespace": "workspace-1",
                        "resourceVersion": "1074",
                        "uid": "cf4fca9d-8541-429f-be85-e50afb036442",
                    },
                    "type": "Opaque",
                },
            },
            {
                "filterResult": None,
                "object": {
                    "apiVersion": "v1",
                    "data": {"test": "true"},
                    "kind": "Secret",
                    "metadata": {
                        "annotations": {
                            "kubectl.kubernetes.io/last-applied-configuration": '{"apiVersion":"v1","data":{"test":"true"},"kind":"Secret","metadata":{"annotations":{},"name":"test-secret-2","namespace":"workspace-1"},"type":"Opaque"}\\n'
                        },
                        "creationTimestamp": "2022-11-06T03:28:27Z",
                        "managedFields": [
                            {
                                "apiVersion": "v1",
                                "fieldsType": "FieldsV1",
                                "fieldsV1": {
                                    "f:data": {".": {}, "f:test": {}},
                                    "f:metadata": {
                                        "f:annotations": {
                                            ".": {},
                                            "f:kubectl.kubernetes.io/last-applied-configuration": {},
                                        }
                                    },
                                    "f:type": {},
                                },
                                "manager": "kubectl-client-side-apply",
                                "operation": "Update",
                                "time": "2022-11-06T03:28:27Z",
                            }
                        ],
                        "name": "test-secret-2",
                        "namespace": "workspace-1",
                        "resourceVersion": "1075",
                        "uid": "83467866-de09-4af3-aac2-3324d51fcc73",
                    },
                    "type": "Opaque",
                },
            },
            {
                "filterResult": None,
                "object": {
                    "apiVersion": "v1",
                    "data": {"test": "true"},
                    "kind": "Secret",
                    "metadata": {
                        "annotations": {
                            "kubectl.kubernetes.io/last-applied-configuration": '{"apiVersion":"v1","data":{"test":"true"},"kind":"Secret","metadata":{"annotations":{},"name":"test-secret-3","namespace":"workspace-1"},"type":"Opaque"}\\n'
                        },
                        "creationTimestamp": "2022-11-06T03:28:27Z",
                        "managedFields": [
                            {
                                "apiVersion": "v1",
                                "fieldsType": "FieldsV1",
                                "fieldsV1": {
                                    "f:data": {".": {}, "f:test": {}},
                                    "f:metadata": {
                                        "f:annotations": {
                                            ".": {},
                                            "f:kubectl.kubernetes.io/last-applied-configuration": {},
                                        }
                                    },
                                    "f:type": {},
                                },
                                "manager": "kubectl-client-side-apply",
                                "operation": "Update",
                                "time": "2022-11-06T03:28:27Z",
                            }
                        ],
                        "name": "test-secret-3",
                        "namespace": "workspace-1",
                        "resourceVersion": "1076",
                        "uid": "1ee457cf-1a01-4197-ac31-89f07e2c836e",
                    },
                    "type": "Opaque",
                },
            },
        ],
        "type": "Synchronization",
    }
]

EVENT_SINGLE = [
    {
        "binding": "kubernetes",
        "filterResult": None,
        "object": {
            "apiVersion": "v1",
            "data": {"test": "true"},
            "kind": "Secret",
            "metadata": {
                "annotations": {
                    "kubectl.kubernetes.io/last-applied-configuration": '{"apiVersion":"v1","data":{"test":"true"},"kind":"Secret","metadata":{"annotations":{},"name":"test-secret-7","namespace":"workspace-1"},"type":"Opaque"}\\n'
                },
                "creationTimestamp": "2022-11-06T03:33:11Z",
                "managedFields": [
                    {
                        "apiVersion": "v1",
                        "fieldsType": "FieldsV1",
                        "fieldsV1": {
                            "f:data": {".": {}, "f:test": {}},
                            "f:metadata": {
                                "f:annotations": {
                                    ".": {},
                                    "f:kubectl.kubernetes.io/last-applied-configuration": {},
                                }
                            },
                            "f:type": {},
                        },
                        "manager": "kubectl-client-side-apply",
                        "operation": "Update",
                        "time": "2022-11-06T03:33:11Z",
                    }
                ],
                "name": "test-secret-7",
                "namespace": "workspace-1",
                "resourceVersion": "1478",
                "uid": "e9fecca5-f4e0-4a70-9b7d-38ddffe00f8c",
            },
            "type": "Opaque",
        },
        "type": "Event",
        "watchEvent": "Added",
    }
]

EVENT_MULTIPLE = [
    {
        "binding": "kubernetes",
        "filterResult": None,
        "object": {
            "apiVersion": "v1",
            "data": {"test": "true"},
            "kind": "Secret",
            "metadata": {
                "annotations": {
                    "kubectl.kubernetes.io/last-applied-configuration": '{"apiVersion":"v1","data":{"test":"true"},"kind":"Secret","metadata":{"annotations":{},"name":"test-secret-4","namespace":"workspace-1"},"type":"Opaque"}\\n'
                },
                "creationTimestamp": "2022-11-06T03:30:50Z",
                "managedFields": [
                    {
                        "apiVersion": "v1",
                        "fieldsType": "FieldsV1",
                        "fieldsV1": {
                            "f:data": {".": {}, "f:test": {}},
                            "f:metadata": {
                                "f:annotations": {
                                    ".": {},
                                    "f:kubectl.kubernetes.io/last-applied-configuration": {},
                                }
                            },
                            "f:type": {},
                        },
                        "manager": "kubectl-client-side-apply",
                        "operation": "Update",
                        "time": "2022-11-06T03:30:50Z",
                    }
                ],
                "name": "test-secret-4",
                "namespace": "workspace-1",
                "resourceVersion": "1276",
                "uid": "8f2d0169-86c6-4aa1-a8eb-d652a0d1878d",
            },
            "type": "Opaque",
        },
        "type": "Event",
        "watchEvent": "Added",
    },
    {
        "binding": "kubernetes",
        "filterResult": None,
        "object": {
            "apiVersion": "v1",
            "data": {"test": "true"},
            "kind": "Secret",
            "metadata": {
                "annotations": {
                    "kubectl.kubernetes.io/last-applied-configuration": '{"apiVersion":"v1","data":{"test":"true"},"kind":"Secret","metadata":{"annotations":{},"name":"test-secret-5","namespace":"workspace-1"},"type":"Opaque"}\\n'
                },
                "creationTimestamp": "2022-11-06T03:30:50Z",
                "managedFields": [
                    {
                        "apiVersion": "v1",
                        "fieldsType": "FieldsV1",
                        "fieldsV1": {
                            "f:data": {".": {}, "f:test": {}},
                            "f:metadata": {
                                "f:annotations": {
                                    ".": {},
                                    "f:kubectl.kubernetes.io/last-applied-configuration": {},
                                }
                            },
                            "f:type": {},
                        },
                        "manager": "kubectl-client-side-apply",
                        "operation": "Update",
                        "time": "2022-11-06T03:30:50Z",
                    }
                ],
                "name": "test-secret-5",
                "namespace": "workspace-1",
                "resourceVersion": "1277",
                "uid": "dc04b86c-94c1-495c-8218-d269ec5f483f",
            },
            "type": "Opaque",
        },
        "type": "Event",
        "watchEvent": "Added",
    },
    {
        "binding": "kubernetes",
        "filterResult": None,
        "object": {
            "apiVersion": "v1",
            "data": {"test": "true"},
            "kind": "Secret",
            "metadata": {
                "annotations": {
                    "kubectl.kubernetes.io/last-applied-configuration": '{"apiVersion":"v1","data":{"test":"true"},"kind":"Secret","metadata":{"annotations":{},"name":"test-secret-6","namespace":"workspace-1"},"type":"Opaque"}\\n'
                },
                "creationTimestamp": "2022-11-06T03:30:50Z",
                "managedFields": [
                    {
                        "apiVersion": "v1",
                        "fieldsType": "FieldsV1",
                        "fieldsV1": {
                            "f:data": {".": {}, "f:test": {}},
                            "f:metadata": {
                                "f:annotations": {
                                    ".": {},
                                    "f:kubectl.kubernetes.io/last-applied-configuration": {},
                                }
                            },
                            "f:type": {},
                        },
                        "manager": "kubectl-client-side-apply",
                        "operation": "Update",
                        "time": "2022-11-06T03:30:50Z",
                    }
                ],
                "name": "test-secret-6",
                "namespace": "workspace-1",
                "resourceVersion": "1278",
                "uid": "b0662d33-bf41-431e-9f06-61fc0c99cd92",
            },
            "type": "Opaque",
        },
        "type": "Event",
        "watchEvent": "Added",
    },
]
