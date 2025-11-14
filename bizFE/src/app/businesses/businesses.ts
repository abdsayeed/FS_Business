import { Component, OnInit } from '@angular/core';
import { BusinessData } from '../services/business-data';
import { RouterOutlet, RouterModule } from '@angular/router';

@Component({
  selector: 'app-businesses',
  imports: [RouterOutlet, RouterModule],
  providers: [BusinessData],
  templateUrl: './businesses.html',
  styleUrl: './businesses.css',
})
export class Businesses implements OnInit {
  business_list: any[] = [];
  page: number = 1; // start on page 1

  constructor(protected businessData: BusinessData) {}

  ngOnInit() {
    if (sessionStorage['page']) {
      this.page = Number(sessionStorage['page']);
    }
    this.business_list = this.businessData.getBusinesses(this.page);
  }

  previousPage() {
    if (this.page > 1) {
      this.page = this.page - 1;
      sessionStorage['page'] = this.page;
      this.business_list = this.businessData.getBusinesses(this.page);
      sessionStorage['page'] = this.page;
    }
  }

  nextPage() {
    if (this.page < this.businessData.getLastPageNumber()) {
      this.page = this.page + 1;
      sessionStorage['page'] = this.page;
      this.business_list = this.businessData.getBusinesses(this.page);
      sessionStorage['page'] = this.page;
    }
  }
}
