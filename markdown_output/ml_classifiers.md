## Overview

This package provides a ROS service for interfacing with various machine
learning algorithms for supervised classification. Three example
classifiers are included, including a nearest neighbor and support
vector machine classifier, but additional classifiers can be added
easily though [pluginlib](http://www.ros.org/wiki/pluginlib).

## Installation



```
$ sudo apt-get install ros-fuerte-ml-classifiers
```

 

```
$ sudo apt-get install ros-groovy-ml-classifiers
```




```
$ sudo apt-get install ros-hydro-ml-classifiers
```



## ROS API

ml_classifiers provides a general interface for all plugin classifiers
to implement:



```clearsilver
name = Interface
srv {
  0.name = ml_classifiers/add_class_data
  0.type = ml_classifiers/AddClassData
  0.desc = Add supplied training data to the specified classifier.
  1.name = ml_classifiers/classify_data
  1.type = ml_classifiers/ClassifyData
  1.desc = Use the specified classifier to classify new data points.
  2.name = ml_classifiers/clear_classifier
  2.type = ml_classifiers/ClearClassifier
  2.desc = Clear all training data from specified classifier.
  3.name = ml_classifiers/create_classifier
  3.type = ml_classifiers/CreateClassifier
  3.desc = Create a new classifier of specified type and name. Overwrites existing classifier of same name if it exists.
  4.name = ml_classifiers/load_classifier
  4.type = ml_classifiers/LoadClassifier
  4.desc = Load classifier data from file.
  5.name = ml_classifiers/save_classifier
  5.type = ml_classifiers/SaveClassifer
  5.desc = Save classifier data to file.
  6.name = ml_classifiers/train_classifier
  6.type = ml_classifiers/TrainClassifier
  6.desc = Train classifier using available training data.
}
```



## Plugins

ml_classifiers comes with 3 plugins built in: A "zero" classifier that
classifies everything as class 0 no matter what, a nearest neighbor
classifier, and an SVM classifier based on
[libSVM](http://www.csie.ntu.edu.tw/~cjlin/libsvm/). More classifiers
can be added easily though
[pluginlib](http://www.ros.org/wiki/pluginlib) and by implementing the
above interface.

## Usage

Simply compile all additional desired plugins and then:



```
$ roslaunch ml_classifiers classifier_server.launch
```

 An example python script to wrap the service
calls and test the SVM classifier:



```python
import roslib; roslib.load_manifest('ml_classifiers')
import rospy
import ml_classifiers.srv
import ml_classifiers.msg

#Wrapper for calls to ROS classifier service and management of classifier data
class ClassifierWrapper:

    def __init__(self):
        #Set up Classifier service handles
        print 'Waiting for Classifier services...'
        rospy.wait_for_service("/ml_classifiers/create_classifier")
        self.add_class_data = rospy.ServiceProxy(
            "/ml_classifiers/add_class_data",
            ml_classifiers.srv.AddClassData, persistent=True)
        self.classify_data = rospy.ServiceProxy(
            "/ml_classifiers/classify_data",
            ml_classifiers.srv.ClassifyData, persistent=True)
        self.clear_classifier = rospy.ServiceProxy(
            "/ml_classifiers/clear_classifier",
            ml_classifiers.srv.ClearClassifier, persistent=True)
        self.create_classifier = rospy.ServiceProxy(
            "/ml_classifiers/create_classifier",
            ml_classifiers.srv.CreateClassifier, persistent=True)
        self.load_classifier = rospy.ServiceProxy(
            "/ml_classifiers/load_classifier",
            ml_classifiers.srv.LoadClassifier, persistent=True)
        self.save_classifier = rospy.ServiceProxy(
            "/ml_classifiers/save_classifier",
            ml_classifiers.srv.SaveClassifier, persistent=True)
        self.train_classifier = rospy.ServiceProxy(
            "/ml_classifiers/train_classifier",
            ml_classifiers.srv.TrainClassifier, persistent=True)
        print 'OK\n'


    def addClassDataPoint(self, identifier, target_class, p):
        req = ml_classifiers.srv.AddClassDataRequest()
        req.identifier = identifier
        dp = ml_classifiers.msg.ClassDataPoint()
        dp.point = p
        dp.target_class = target_class
        req.data.append(dp)
        resp = self.add_class_data(req)


    def addClassDataPoints(self, identifier, target_classes, pts):
        req = ml_classifiers.srv.AddClassDataRequest()
        req.identifier = identifier
        for i in xrange(len(pts)):
            dp = ml_classifiers.msg.ClassDataPoint()
            dp.point = pts[i]
            dp.target_class = target_classes[i]
            req.data.append(dp)
        resp = self.add_class_data(req)


    def classifyPoint(self, identifier, p):
        req = ml_classifiers.srv.ClassifyDataRequest()
        req.identifier = identifier
        dp = ml_classifiers.msg.ClassDataPoint()
        dp.point = p
        req.data.append(dp)
        resp = self.classify_data(req)
        return resp.classifications[0]


    def classifyPoints(self, identifier, pts):
        req = ml_classifiers.srv.ClassifyDataRequest()
        req.identifier = identifier
        for p in pts:
            dp = ml_classifiers.msg.ClassDataPoint()
            dp.point = p
            req.data.append(dp)

        resp = self.classify_data(req)
        return resp.classifications


    def clearClassifier(self, identifier):
        req = ml_classifiers.srv.ClearClassifierRequest()
        req.identifier = identifier
        resp = self.clear_classifier(req)


    def createClassifier(self, identifier, class_type):
        req = ml_classifiers.srv.CreateClassifierRequest()
        req.identifier = identifier
        req.class_type = class_type
        resp = self.create_classifier(req)


    def loadClassifier(self, identifier, class_type, filename):
        req = ml_classifiers.srv.LoadClassifierRequest()
        req.identifier = identifier
        req.class_type = class_type
        req.filename = filename
        resp = self.load_classifier(req)


    def saveClassifier(self, identifier, filename):
        req = ml_classifiers.srv.SaveClassifierRequest()
        req.identifier = identifier
        req.filename = filename
        resp = self.save_classifier(req)


    def trainClassifier(self, identifier):
        req = ml_classifiers.srv.TrainClassifierRequest()
        req.identifier = identifier
        resp = self.train_classifier(req)


if __name__ == '__main__':
    cw = ClassifierWrapper()
    cw.createClassifier('test','ml_classifiers/SVMClassifier')

    targs = ['1','1','2','2','3']
    pts = [[0.1,0.2],[0.3,0.1],[3.1,3.2],[3.3,4.1],[5.1,5.2]]
    cw.addClassDataPoints('test', targs, pts)
    cw.trainClassifier('test')

    testpts = [[0.0,0.0],[5.5,5.5],[2.9,3.6]]
    resp = cw.classifyPoints('test',testpts)
    print resp
```



## Report a Bug
