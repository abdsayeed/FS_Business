import { Component, OnInit } from '@angular/core';
import { BusinessData } from '../../services/business-data';
import { ActivatedRoute } from '@angular/router';

@Component({
  selector: 'app-business',
  imports: [],
  providers: [BusinessData],
  templateUrl: './business.html',
  styleUrl: './business.css',
})
export class Business implements OnInit {
  business_list: any[] = [];

  constructor(private route: ActivatedRoute,
    private businessData: BusinessData) {}

  ngOnInit() {
    const id = this.route.snapshot.paramMap.get('id');
    if (id) {
      this.business_list = this.businessData.getBusiness(id);
    }
  }
}
