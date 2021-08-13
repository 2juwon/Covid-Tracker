import 'package:flutter/material.dart';
import 'package:naver_map_plugin/naver_map_plugin.dart';

class MapPage extends StatelessWidget {
  // This widget is the root of your application.
  @override
  Widget build(BuildContext context) {
    return MaterialApp(
      title: 'Covid Tracker',
      home: NaverMap(
        initialCameraPosition: CameraPosition(
          target: LatLng(35.3226551, 127.7861468),
          zoom: 17,
        ),
        initLocationTrackingMode:
        LocationTrackingMode.NoFollow,
        mapType: MapType.Basic,
      ),
    );
  }
}
