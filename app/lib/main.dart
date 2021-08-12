import 'package:flutter/material.dart';
import 'package:naver_map_plugin/naver_map_plugin.dart';

void main() {
  runApp(MyApp());
}

class MyApp extends StatelessWidget {
  // This widget is the root of your application.
  @override
  Widget build(BuildContext context) {
    return MaterialApp(
      title: 'Covid Tracker',
      home: NaverMap(
        initialCameraPosition: CameraPosition(
          target: LatLng(37.566570, 126.978442),
          zoom: 17,
        ),
        initLocationTrackingMode:
        LocationTrackingMode.NoFollow,
      ),
    );
  }
}
