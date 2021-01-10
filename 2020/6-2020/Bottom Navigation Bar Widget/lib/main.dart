import 'package:flutter/material.dart';
import 'package:bottom_navigation_bar/nav.dart';

void main() {
  runApp(MyApp());
}

class MyApp extends StatelessWidget {
  @override
  Widget build(BuildContext context) {
    return MaterialApp(
      title: 'Bottom Navigation Bar Tutorial',
      home: Nav(),
    );
  }
}