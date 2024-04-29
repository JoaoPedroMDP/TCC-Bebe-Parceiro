import { ComponentFixture, TestBed } from '@angular/core/testing';

import { ListPendingProfessionalsComponent } from './list-pending-professionals.component';

describe('ListPendingProfessionalsComponent', () => {
  let component: ListPendingProfessionalsComponent;
  let fixture: ComponentFixture<ListPendingProfessionalsComponent>;

  beforeEach(async () => {
    await TestBed.configureTestingModule({
      declarations: [ ListPendingProfessionalsComponent ]
    })
    .compileComponents();

    fixture = TestBed.createComponent(ListPendingProfessionalsComponent);
    component = fixture.componentInstance;
    fixture.detectChanges();
  });

  it('should create', () => {
    expect(component).toBeTruthy();
  });
});
