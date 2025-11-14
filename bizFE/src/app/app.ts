import { Component, signal } from '@angular/core';
import { Businesses } from './businesses/businesses';
import { RouterOutlet } from '@angular/router';

@Component({
  selector: 'app-root',
  imports: [RouterOutlet, Businesses],
  templateUrl: './app.html',
  styleUrl: './app.css'
})
export class App {
  protected readonly title = signal('bizFE');
}
